program z19_21;
const 
    limit: integer = 808;
var
    matrix: array[1..3*limit, 1..3*limit] of integer;
    negativeNumbers: List<integer>;


begin
    for var x := 1 to 3*limit do
        for var y := 1 to 3*limit do
            matrix[x, y] := 0;
    for var x := limit - 1 downto 1 do
        for var y := limit - x - 1 downto 1 do begin
            var positions : array of integer = (matrix[x+2, y], matrix[x, y+2], matrix[3*x, y], matrix[x, 3*y]);
            negativeNumbers := new List<integer>;
            
            foreach i: integer in positions do
                if i <= 0 then negativeNumbers.Add(i);
            if negativeNumbers.Count > 0 then matrix[x, y] := -negativeNumbers.Max + 1
            else matrix[x, y] := -positions.Max;
        end;
    for var i := 1 to limit do
        WriteLn(i, matrix[35, i]:8);
end.
