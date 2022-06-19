@echo off
cls
:menu
cls
color 90

cls
date /t
echo Computador: %computername% Usuario: %username%                   
echo        Simpe Vote Laucher
echo  ==================================
echo * 1.Modulo de Contagem            * 
echo * 2.Modulo de Injecao             *
echo * 3.Modulo de Votacao             * 
echo * 4.Sobre                         *
echo * 5.Sair                          * 
echo  ==================================                      

set /p opcao= Escolha uma opcao: 
echo ------------------------------
if %opcao% equ 1 goto iniciarg
if %opcao% equ 2 goto primeror
if %opcao% equ 3 goto ajudap
if %opcao% equ 4 goto sobrep
if %opcao% equ 5 goto sair
if %opcao% GEQ 6 goto erro

:iniciarg
cls
echo ==================================
echo *           Iniciado             *
echo ==================================
python .\mod3.py
pause
goto menu

:primeror
cls
echo ==================================
echo *           Iniciado             *
echo ==================================
python .\mod2.py
pause
goto menu


:ajudap
cls
echo ==================================
echo *           Iniciado             *
echo ==================================
python .\mod1.py
pause
goto menu


:sobrep
cls
echo ==================================
echo *Craido Por Ruaneri Portela para *
echo *a atividade de primeiro semestre*
echo *da materia de AED da FURG       *
echo *12/2021 Santarem/Para/Brasil    *
echo ==================================
pause
goto menu

:sair
cls
pause
exit

:erro
echo ==============================================
echo * Opcao Invalida! Escolha outra opcao do menu *
echo ==============================================
pause
goto menu
