INSERT INTO records(sitename,county,aqi,status,pm25,date,lat,lon)
values('屏東(枋山)','屏東',17,'良好',10,'2024-10-28 13:00',22.260899,120.651472)

SELECT DISTINCT sitename
from records

SELECT date,county,aqi,pm25,status,lat,lon 
FROM records 
WHERE sitename=?
ORDER BY date DESC ;
/*asc:accend*/

SELECT date,county,aqi,pm25,status,lat,lon 
FROM records 
WHERE sitename='林口';
