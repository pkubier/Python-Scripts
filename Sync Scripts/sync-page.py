from dirsync import sync

source_path = '//uco.local/web-prod/bronchoanalytics.uco.edu/UCO'
target_path = '//uco.local/web-prod/bronchoanalytics.uco.edu/'
pattern = ('inactive-program-inventory*','budget*','nav*','inprogress*','majors-conferred*','settings*','header*','test*','majors-enrollment2*','minors-conferred2*','favicon*','index*','images*','assets','audio*','code*','files*','jscharts','UCO','data','Provost','thumbnails','_Old','credit*','applications*','browswer*','concurrent*','export*','faculty-credit*','faculty-degree*','faculty-dept*','faculty-fte*','faculty-sections','online*','search*','student-demo-*','student-hs*','us*','zoom*','total*','student-transfer*')
pattern2 =('active-program-inventory*','assessment*', 'program-inv*','user-notes*','cirptfs*','enrollment*','faculty-chars*','footer*','gos*','gss*','ipeds*','majors*','minors*','mission*','ncha*','nsse*','peergroups*','program*','ruffalo*','secure*','staff*','stlr*')

sync(source_path, target_path, 'sync', verbose=True, include=pattern2, exclude=pattern)
