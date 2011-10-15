import csv
r = csv.reader(open('akb48.csv'))
fields = r.next()
for _row in r:
    row = dict((k, unicode(_row[i], 'utf-8')) for i, k in enumerate(fields))
    birth_year, birth_month, birth_day = [int(c) for c in row['birthday'].split('-')]
    file = u'''# encoding: utf-8
import datetime

__all__ = [
    'info',
    ]

def info():
    return {
        'birthday':         datetime.date(%(birth_year)d, %(birth_month)d, %(birth_day)d),
        'class':            u'%(class)s',
        'family_name_en':   u'%(family_name_en)s',
        'family_name_kana': u'%(family_name_kana)s',
        'first_name_en':    u'%(first_name_en)s',
        'first_name_kana':  u'%(first_name_kana)s',
        'graduate_date':    %(graduate_date)s,
        'hometown':         u'%(hometown)s',
        'name_en':          u'%(name_en)s',
        'name_ja':          u'%(name_ja)s',
        'name_kana':        u'%(name_kana)s',
        'nick':             u'%(nick)s',
        'team':             %(team)s,
        }
''' % {
        'birth_year': birth_year,
        'birth_month': birth_month,
        'birth_day': birth_day,
        'class': row['class'],
        'family_name_en': row['family_name_en'],
        'family_name_kana': row['family_name_kana'],
        'first_name_en': row['first_name_en'],
        'first_name_kana': row['first_name_kana'],
        'graduate_date': u"datetime.date(%d, %d, %d)" % tuple(int(c) for c in row['graduate_date'].split(u'-')) if row['graduate_date'] else u'None',
        'hometown': row['hometown'],
        'name_en': u'%s %s' % tuple(k.title() for k in (row['family_name_en'], row['first_name_en'])),
        'name_ja': row['name_ja'],
        'name_kana': u'%s %s' % (row['family_name_kana'], row['first_name_kana']),
        'nick': row['nick'],
        'team': u"u'%s'" % row['team'] if row['team'] else u'None',
        }
    try:
        filename = str('%s_%s.py' % (row['family_name_en'], row['first_name_en']))
        open('akb48/member/%s' % filename, 'w').write(file.encode('utf-8'))
    except:
        print row
