{game logic - execution of all commands recognized by the game}

procedure execute(action, target: Shortint);
var R: Registers;
    unknown: Boolean;

    procedure message_short(n: Byte);
        begin output_multiliner(texts_short[n], 1, 2);
        unknown := False end;

    procedure message_middle(n: Byte);
        begin output_multiliner(texts_middle[n], 1, 2);
        unknown := False end;

    procedure message(n: Byte);
        begin output_multiliner(texts_other[n], 1, 2);
        unknown := False end;

    begin
    case action of
        0: {Zkoumej} begin
            output_multiliner(things[target].desc, 1, 2);
            if (target = 2{mrtvola}) and (things[10{hajzlpapir}].where = 51)
                    and (things[13{drat}].where = 49) then
                add_to_room(13{drat}) end;

        1: {Jdi} begin
            Delay(150);
            room := target;
            moved := True end;

        2: {Vezmi} begin
            if target = 4{oci} then begin
                things[4].portable := False;
                add_to_inventory(20{oko}) end
            else begin
                remove_from_room(target);
                add_to_inventory(target);

                case target of
                    13: {drat}
                        things[2{mrtvola}].desc := temp_desc;
                    14: {pavucina}
                        add_to_room(11{pavouk}) end end;

            case target of
                4: {oci}
                    message_short(4);
                14: {pavucina}
                    message(5)
                else
                    message_short(0{Budiz}) end end;

        3: {Pouzij} begin
            unknown := True;
            case target of
                5: {jehla}
                    if (room = 0) and (things[13{drat}].where in [50, 51]) then begin
                    remove_from_inventory(5);
                    message(14) end;
                6: {licidla} begin
                    remove_from_inventory(6);
                    message(6) end;
                7: {bryle} begin
                    cga_palette := 1 - cga_palette;
                    R.AX := $0b00;
                    R.BX := $0100 + cga_palette;
                    Intr($10, R);
                    if cga_palette = 0 then
                        message_short(3)
                    else
                        message_short(2) end;
                8: {pila}
                    if (room = 19) and (things[19{jed}].where = 51) then begin
                        remove_from_inventory(8);
                        things[21{ruka}].portable := True;
                        message(12) end;
                10: {hajzlpapir}
                    if (room = 0) and not (2 in openables) then begin
                        remove_from_inventory(10);
                        temp_desc := things[2{mrtvola}].desc;
                        things[2{mrtvola}].desc := texts_other[3];
                        message(2) end;
                11: {pavouk}
                    if things[16{recepcni}].where = room then begin
                        remove_from_inventory(11);
                        remove_from_room(16{recepcni});
                        room_exits[room] := '9H'{9,24};
                        message(7) end;
                12: {zuby}
                    if (room = 7) and (things[12{zuby}].where <> 51) then begin
                        remove_from_inventory(12);
                        add_to_room(15{ziletka});
                        Delete(things[3{skladnik}].desc, 30, 19);
                        message(9) end;
                13: {drat}
                    if room = 23 then begin
                        remove_from_inventory(13);
                        things[14{pavucina}].where := room;
                        things[0{lucerna}].image := @SVITI;
                        things_in_room;
                        Delete(things[0{lucerna}].desc, 27, 53);
                        things[18{uklizecka}].where := 15;
                        things[18{uklizecka}].desc := texts_other[16];
                        room_exits[15] := '>'{14};
                        message(4) end;
                14: {pavucina}
                    if room = 15 then begin
                        remove_from_inventory(14);
                        remove_from_room(18{uklizecka});
                        room_exits[15] := '>@'{14,16};
                        message(15) end;
                15: {ziletku}
                    if (room = 0) and not (things[15{ziletka}].where = 51) then begin
                        remove_from_inventory(15);
                        message(0) end;
                17: {otvirak}
                    if room = 5 then begin
                        remove_from_inventory(17);
                        message_middle(1) end;
                19: {jed}
                    if room = 19 then begin
                        remove_from_inventory(19);
                        add_to_room(21{ruka});
                        things[9{reditel}].desc := Copy(things[9].desc, 1, 60) + texts_short[9];
                        message(11) end;
                20: {oko}
                    if (things[18{uklizecka}].where = room)
                            and (things[6{licidla}].where = 51) then begin
                        remove_from_inventory(20{oko});
                        remove_from_room(18{uklizecka});
                        add_to_room(23{klic});
                        add_to_room(26{smetak});
                        room_exits[room] := ';='{11,13};
                        message(10) end;
                21: {ruka}
                    if room = 10 then begin
                        remove_from_inventory(21);
                        room_exits[room] := 'G;'{23,11};
                        room_descriptions[room][42] := '!';
                        room_descriptions[room][58] := '^';
                        room_descriptions[room][68] := '!';
                        Delete(room_descriptions[room], 33, 10);
                        message_short(6) end;
                23: {klic}
                    if room = 18 then begin
                        remove_from_inventory(23);
                        room_exits[room] := 'A9'{17,9};
                        room_descriptions[room][51] := '!';
                        room_descriptions[room][64] := '^';
                        room_descriptions[room][75] := '!';
                        Delete(room_descriptions[room], 30, 10);
                        message_short(5) end
                    else if room = 10 then
                        message(13);
                24: {femur}
                    if room = 3 then begin
                        remove_from_inventory(24);
                        message_middle(3) end;
                26: {smetak}
                    if room = 8 then begin
                        remove_from_inventory(26);
                        add_to_room(24{femur});
                        add_to_room(27{zub});
                        message_middle(2) end end;

            if unknown then
                message_short(1{Nevim jak}) end;

        4: {Otevri} begin
            unknown := True;
            case target of
                1: {rakev}
                    if things[17{otvirak}].where <> 51 then
                        message_middle(0)
                    else if (1 in openables) then begin
                        openables := openables - [1];
                        things[12{zuby}].where := room;
                        things[1].image := @BEZVIKA;
                        things_in_room;
                        message(8) end;
                2: {mrtvolu}
                    if (things[15{ziletka}].where = 51) and (2 in openables) then begin
                        openables := openables - [2];
                        message(1) end;
                25: {skrin}
                    if things[24{femur}].where <> 51 then
                        message_short(7)
                    else if (25 in openables) then begin
                        openables := openables - [25];
                        things[19{jed}].where := room;
                        things[25].image := @OTEVRENA;
                        things_in_room;
                        message_middle(4) end end;

            if unknown then
                message_short(1{Nevim jak}) end;

        5: {Konec}
            if target = 0 then
                game_end := True end end;
