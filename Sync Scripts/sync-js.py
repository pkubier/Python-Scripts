from dirsync import sync

source_path = '//uco.local/web-prod/bronchoanalytics.uco.edu/UCO/jscharts'
target_path = '//uco.local/web-prod/bronchoanalytics.uco.edu/jscharts'
pattern = ('demo-student-all*','chart*','us*','world*','university*','files*','credit*','export*','hs*','online*','provost*','state*','concurrent*','jquery*','demo-student*',)
pattern2 =('demo-faculty*','demo-student-age*', 'cirptfs*', 'cirptfs2*','cirpyfcy*','cirpyfcy2*','degree-conferred*','demo-student-all*','enrollment*','enrollment2','gos*','gss*','ipedsadmissions*','ipedsawards*','ipedsenrollment*','ipedsfinaid*','ipedsfinance*','ipedslibrary*','ipedsprice*','ipedsretention*','ipedsstaff*','minor-conferred*','ncha*','nsse*','ruffalo*','staff*','stlr*',)

sync(source_path, target_path, 'sync', verbose=True, exclude=pattern, include=pattern2)
