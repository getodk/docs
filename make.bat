@ECHO OFF

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=python -msphinx
)

set ODKX_SRCDIR=odkx-src
set COMPILE_X_SRCDIR=tmpx-src
set ODKX_BUILDDIR=odkx-build

if "%1" == "clean" goto cleancmd
if "%1" == "copy" goto copy
if "%1" == "odkx" goto odkx
if "%1" == "odkx-latex" goto odkx-latex
ECHO Supported commands are: clean, copy, odkx, odkx-latex
goto end

:cleancmd
:copy
:odkx
:odkx-latex
del /F /Q /S %COMPILE_X_SRCDIR%
del /F /Q /S %ODKX_BUILDDIR%
if "%1" == "clean" goto end
mkdir %COMPILE_X_SRCDIR%
xcopy %ODKX_SRCDIR% %COMPILE_X_SRCDIR% /E /H
if "%1" == "copy" goto end
%SPHINXBUILD% -b dirhtml %COMPILE_X_SRCDIR% %ODKX_BUILDDIR%
if "%1" == "odkx" goto end
%SPHINXBUILD% -b latex %COMPILE_X_SRCDIR% %ODKX_BUILDDIR%\latex

:end
