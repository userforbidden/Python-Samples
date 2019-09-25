text = 'nlaebolkoballoon'
ans = len(text)
for l in 'ban':
    ans = min(ans,text.count(l))
for l in 'lo':
    ans= min(ans,text.count(l))

print(ans)