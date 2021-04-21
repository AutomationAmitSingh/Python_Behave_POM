# Python_Behave_POM
1.Behave –f allure behave.formatter:AllureFormatter –o name of report folder you want” 
[Path where your features are present]

2. To Generate report ;
Allure generate [path where reports are present]

3. To Open :
allure open [path where index file is present]

------------------------------------------------------------------------------------------------
1
behave -D ARCHIVE=Yes -D BROWSER=firefox features\login_Concert.feature -f allure_behave.formatter:AllureFormatter -o %allure_result_folder%
%allure_result_folder% = any folder name
2
allure generate Reports --clean 
3
allure open ./allure-report/ 
4
allure serve %allure_result_folder% This command directly generate report in user temp folder and run jetty and display index.html file on browser
