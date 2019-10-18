procedure decode_and_write(x: Word; y: Byte; input_text: string);
var i, n: Byte;

const codes: array[$c0..$dd] of Byte = (
{$I KODY.PAS}
);
      letters: string = 'ACDEINORSTUYZacdeinorstuyz';

    begin MoveTo(x, y);
    for i := 1 to Length(input_text) do begin
        n := Ord(input_text[i]);
        if n >= $c0 then begin

            {draw diacritic}
            case codes[n] shr 5 of
                0: begin {acute uppercase}
                    Line(GetX + 3, y - 1, GetX + 4, y - 1);
                    Line(GetX + 4, y - 2, GetX + 5, y - 2) end;
                1: begin {caron uppercase}
                    Line(GetX + 4, y - 2, GetX + 3, y - 1);
                    Line(GetX + 3, y - 1, GetX + 2, y - 2) end;
                2: {ring uppercase U}
                    Circle(GetX + 3, y - 2, 1);
                3: begin {acute lowercase}
                    Line(GetX + 3, y, GetX + 4, y);
                    Line(GetX + 4, y - 1, GetX + 5, y - 1) end;
                4: begin {caron lowercase}
                    Line(GetX + 2, y - 1, GetX + 3, y - 1);
                    Line(GetX + 3, y, GetX + 4, y);
                    Line(GetX + 5, y - 1, GetX + 5, y - 1) end;
                5: {ring lowercase u}
                    Circle(GetX + 3, y, 1);
                6: {caron d}
                    Line(GetX + 7, y + 1, GetX + 8, y) end;

            {draw letter}
            OutText(letters[codes[n] and $1f]) end

        else if (n >= $20) and (n <= $7d) then
            OutText(Chr(n xor 1))

        else
            OutText(input_text[i]) end end;


procedure output_multiliner(input_text: string; fg, row: Byte);
var i, y: Byte;
    single_line: string;

    begin SetFillStyle(SolidFill, 0);
    Bar(47, 55 + 10*row, 271, 121);

    if fg = 1 then
        room_desc_visible := False;

    SetColor(fg);
    y := 60 + 10*row;

    repeat
        i := Pos('^'{line break}, input_text);

        if i > 0 then begin
            {write one line and trim input_text}
            single_line := Copy(input_text, 1, i - 1);
            decode_and_write(160 - 4*Length(single_line), y, single_line);
            input_text := Copy(input_text, i + 1, 256);
            y := y + 10 end
        else begin
            decode_and_write(160 - 4*Length(input_text), y, input_text);
            Break end;

        until False end;


procedure output_oneliner(input_str: string);

    begin SetFillStyle(SolidFill, 0);
    Bar(47, 55, 271, 121);
    SetColor(1);
    decode_and_write(160 - 4*Length(input_str), 60, input_str);
    room_desc_visible := False end;


procedure room_description;

    begin output_multiliner(room_descriptions[room], 2, 0);
    room_desc_visible := True end;


procedure sound_1;
var i: Byte;

    begin
    for i:= 25 to 35 do begin
        Sound(i * 4);
        Delay(1) end;
    NoSound end;


procedure sound_2;
var i: Byte;

    begin
    for i:= 40 downto 30 do begin
        Sound(i * 4);
        Delay(1) end;
    NoSound end;
