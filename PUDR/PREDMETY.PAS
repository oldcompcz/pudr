procedure add_to_inventory(thing_id: Byte);
var i: Byte;

    begin
    for i := 0 to 5 do
        if inventory[i] = -1 then
            Break;

    inventory[i] := thing_id;
    things[thing_id].where := 50;

    PutImage(41 + 40*i, 128, things[thing_id].image^, XORPut) end;


procedure remove_from_inventory(thing_id: Byte);
var i: Byte;

    begin
    for i := 0 to 5 do
        if inventory[i] = thing_id then
            Break;

    inventory[i] := -1;
    things[thing_id].where := 51;

    PutImage(41 + 40*i, 128, things[thing_id].image^, XORPut) end;


function inventory_full: Boolean;
var i: Byte;

    begin inventory_full := True;

    for i := 0 to 5 do
        if inventory[i] = -1 then begin
            inventory_full := False;
            Break end end;


procedure things_in_room;
var thing_id: Byte;

    begin SetFillStyle(SolidFill, 0);
    Bar(101, 10, 218, 47);     
    for thing_id := 0 to thing_count do
        if things[thing_id].where = room then
            PutImage(103 + 38*things[thing_id].slot, 12, things[thing_id].image^, XORPut) end;


procedure add_to_room(thing_id: Byte);

    begin things[thing_id].where := room;
    PutImage(103 + 38*things[thing_id].slot, 12, things[thing_id].image^, XORPut) end;


procedure remove_from_room(thing_id: Byte);

    begin things[thing_id].where := 51;
    PutImage(103 + 38*things[thing_id].slot, 12, things[thing_id].image^, XORPut) end;
