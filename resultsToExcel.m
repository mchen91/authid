% print data

printTable = [];
for i=1:nodeMax
    for j=1:layerMax
        printTable = [printTable;[results(i,j,1) results(i,j,2) results(i,j,3) results(i,j,4) results(i,j,5)]];
    end
end

[PATHSTR3,NAME3,EXT3] = fileparts(mfilename('fullpath'));
fileName3 =  fullfile(PATHSTR3,'backup.xlsx');
xlswrite(fileName3,printTable,'save');
