#!/usr/bin/env python3
from chibi.command import yum, echo

echo.cowsay( "start updating centos" )
yum.update()
yum.install( 'epel-release' )
echo.cowsay( "end updating centos" )
