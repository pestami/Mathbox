//===================================================================
//Plot Graph
//===================================================================
 scf(1) // set graph hanle
//clf()  // clear the graph
 lines(0) //Stops paging prompt
//h=scf(1);
title('Items in Nummernverzichnis')
//=====================================================================
pathnameGraph='X:\SYM_WINCHILL_Download\010-scilab\NV.JPG'
pathnameNV='X:\SYMPHONY_Download\001_LSMW_Feller\backup\Report_count.dat'
//=====================================================================
M = csvRead(pathnameNV ,ascii(9))
//=====================================================================
//y=[12000 12605 1256];

y=M(:,1);
//y=y - 12000;
y=y - 000;

bar(y,0.1,'yellow');
xs2jpg(1,pathnameGraph);
//close(h);
