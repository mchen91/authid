% iter

[PATHSTR2,NAME2,EXT2] = fileparts(mfilename('fullpath'));
fileName2 =  fullfile(PATHSTR2,'authid.m');


nodeMax = 5;
layerMax = 3;
numTests = 5;
results = zeros(nodeMax,layerMax,numTests);
for i=1:nodeMax
    for j=1:layerMax
        for k=1:numTests
            hiddenLayerSize = (5*i)*ones(1,j);
            run(fileName2)
            results(i,j,k)=testPerformance;
            close all;
        end
    end
end

