% iter

[PATHSTR2,NAME2,EXT2] = fileparts(mfilename('fullpath'));
fileName2 =  fullfile(PATHSTR2,'authid.m');


numTests = 10;
results = zeros(numTests,1);
for i=1:numTests
    run(fileName2)
    results(i)=testPerformance;
    close all;
end

mean(results)