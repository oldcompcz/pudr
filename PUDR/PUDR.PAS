program PohrebniUstav;
uses Dos, Crt, Graph, ObjFiles;

type thing = record
               name: string[15];
               where: Shortint;    {49 not yet available, 50 inventory, 51 no longer available}
               portable: Boolean;
               slot: Byte;
               desc: string[89];
               image: Pointer
             end;
     side = (left, top, right, bottom);
     rectangle_region = array[side] of Integer;
     PCommand = ^command;
     command = record
                 name: string[15];
                 action, target: Shortint;
                 region: rectangle_region;
                 next: PCommand
               end;
     mouse_info = record
                    x, y: Integer;
                    left, right: Boolean
                  end;

const {main commands foreground colors}
      cfg: array[0..5] of Byte = (3, 2, 2, 1, 3, 1);
      {main commands background colors}
      cbg: array[0..5] of Byte = (2, 3, 1, 2, 1, 3);
      graph_driver: Integer = CGA;
      graph_mode: Integer = CGAC3;
      action: Shortint = -1;
      target: Shortint = -1;
      game_end: Boolean = False;
      cga_palette: Byte = 1;
      cmd_start: PCommand = nil;
      room: Byte = 0;
      openables: set of Byte = [0, 1, 2, 25];

{$I DATA.PAS}

var mx, my, x_pos: Integer;
    i: Byte;
    destination: Shortint;
    valid_command, moved, room_desc_visible: Boolean;
    top_line, temp_desc: string[87{length of texts_other[3]}];
    mouse: mouse_info;
    cmd: PCommand;
    P: Pointer;
    main_commands: array[1..5] of PCommand;
    inventory: array[0..10] of Shortint;

{$I MYS.PAS}
{$I PREDMETY.PAS}
{$I VYSTUP.PAS}
{$I PRIKAZY.PAS}
{$I LOGIKA.PAS}

begin
RegisterBGIdriver(@CGADriver);
InitGraph(graph_driver, graph_mode, '');
SetBkColor(0);
init_mouse;

for i := 0 to 10 do
    inventory[i] := -1;

{title & intro}
for i := 0 to 6 do begin
    if i = 0 then
        PutImage(91, 57, @TITUL^, XORPut)
    else
        output_multiliner(texts_intro[i - 1], 1 + Ord(i > 3), 0);

    if i = 4 then begin
        PutImage(11, 0, @KAP1H^, XORPut);
        PutImage(11, 117, @KAP1D^, XORPut);
        SetFillStyle(SolidFill, 2);
        Bar(19, 35, 23, 116);
        Setcolor(1);
        Line(24, 35, 24, 116);

        PutImage(54, 0, @KAP2^, XORPut);

        PutImage(236, 0, @KAP3^, XORPut);

        PutImage(286, 0, @KAP4H^, XORPut);
        PutImage(286, 106, @KAP4D^, XORPut);
        SetFillStyle(SolidFill, 1);
        Bar(294, 28, 298, 105);
        Setcolor(2);
        Line(299, 28, 299, 105) end;


    repeat get_mouse_state until mouse.left;
    wait_for_release end;

{show main commands}
x_pos := 0;
for i := 0 to 5 do begin
    add_command(x_pos + 5 + 10*Ord(i=5), 166, cfg[i], cbg[i],
                'text', command_names[i], i, -1, -1);
    if i >= 1 then
        main_commands[i] := last_command end;

repeat    {Main loop}
    room_description;
    if room = 24{game won} then begin
        SetFillStyle(SolidFill, 0);
        Bar(39, 126, 80 + 5*40, 163);
        Bar(3, 164, 316, 196);
        repeat get_mouse_state until mouse.left;
        wait_for_release;
        Break end;

    things_in_room;
    moved := False;

    repeat    {Loop 2 - waiting for movement between rooms}
        valid_command := False;
        top_line := '';

        repeat    {Loop 3 - waiting for a complete action+target command}
            show_mouse;
            cmd := nil;

            repeat    {Loop 4 - waiting for input: a keypress or any clickable being clicked}
                if KeyPressed then
                    case UpCase(ReadKey) of
                        'Z': cmd := cmd_start;
                        'J': cmd := main_commands[1];
                        'V': cmd := main_commands[2];
                        'P': cmd := main_commands[3];
                        'O': cmd := main_commands[4];
                        'K': cmd := main_commands[5] end;
                get_mouse_state;
                if (mouse.x <> mx) or (mouse.y <> my) then begin
                    hide_mouse;
                    show_mouse end;
                if mouse.right and not room_desc_visible then begin
                    hide_mouse;
                    room_description;
                    clear_clickables;
                    action := -1;
                    wait_for_release;
                    show_mouse end;
                if mouse.left then
                    cmd := get_clicked_command
                until cmd <> nil;                     {End of loop 4}

            hide_mouse;

            if cmd^.action <> -1 then begin
                action := cmd^.action;
                target := -1;
                top_line := cmd^.name;
                sound_1 end;
            if cmd^.target <> -1 then begin
                target := cmd^.target;
                top_line := top_line + '!'{space} + cmd^.name;
                sound_2 end;
            if not ((action = 5) and (target = 0)) then
                output_oneliner(top_line);
            wait_for_release;

            if target <> -1 then
                valid_command := True
            else
                case action of
                    0, 2..4: begin
                        set_clickables('things');
                        valid_command := False end;
                    1: begin
                        set_clickables('exits');
                        valid_command := False end;
                    5: begin
                        set_clickables('yes or no');
                        valid_command := False end end
            until valid_command;                      {End of loop 3}
        execute(action, target);
        if game_end then
            Break;
        action := -1;
        target := -1;
        clear_clickables
        until moved;                                  {End of loop 2}
    if game_end then
        Break;
    until False;                                      {End of main loop}

RestoreCrtMode
end.
