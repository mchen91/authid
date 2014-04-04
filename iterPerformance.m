% iter

[PATHSTR2,NAME2,EXT2] = fileparts(mfilename('fullpath'));
fileName2 =  fullfile(PATHSTR2,'authid.m');


nodeMax = 10;
layerMax = 1;
numTests = 2;
results = zeros(nodeMax,layerMax,numTests);
for i=1:nodeMax
    for j=1:layerMax
        for k=1:numTests
            hiddenLayerSize = i*ones(1,j);
            run(fileName2)
            results(i,j,k)=testPerformance;
            close all;
        end
    end
end

