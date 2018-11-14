#-------------------------------------------------------------------------------
# Name:        HW2
# Purpose:     Covert DD to DMS
#
# Author:      Terry Woodard
#
# Created:     11/09/2017
#-------------------------------------------------------------------------------

#DD = d + m/60 + s/3600
#DD = 30.285337
#0.285337*60 =  0.12022*60 =
#d = 30, m = 17, s = 7
def dd2dms(dd):
    d = int(dd)
    md = (dd-d)*60
    m = int(md)
    sd = (md-m)*60
    s = int(sd)

    print 'The coordinate in DMS is: {}d {}m {}s'.format(d,m,s)
