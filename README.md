# kjv-redis-db

Install deps in virtualenv
```bash
ᚱ@redis_kjv $ virtualenv ~/redis_kjv-virt
Using base prefix '/usr'
New python executable in /home/rmintz/redis_kjv-virt/bin/python
Installing setuptools, pip, wheel...
done.
ᚱ@redis_kjv $ source ~/redis_kjv-virt/bin/activate
(redis_kjv-virt) ᚱ@redis_kjv $
(redis_kjv-virt) ᚱ@redis_kjv $
(redis_kjv-virt) ᚱ@redis_kjv $ pip install -r requirements.txt
Collecting redis==2.10.6 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/3b/f6/7a76333cf0b9251ecf49efff635015171843d9b977e4ffcf59f9c4428052/redis-2.10.6-py2.py3-none-any.whl
Installing collected packages: redis
Successfully installed redis-2.10.6
(redis_kjv-virt) ᚱ@redis_kjv $
(redis_kjv-virt) ᚱ@redis_kjv $
```


Create the redis db. Note: Use from the actual directory it lives in.
```bash
(redis_kjv-virt) ᚱ@redis_kjv $ ./create_redis.py
(redis_kjv-virt) ᚱ@redis_kjv $
```


## Example usage of redis bible
```bash
> redis-cli get Genesis:1:1
"In the beginning God created the heaven and the earth."
```

```bash
> redis-cli get John:3:16
"For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."
```


## Cool things you can try with a redis formatted Bible
> Sorted books of the Bible
```bash
redis-cli keys "*" | cut -f1 -d":" | sort | uniq
```
> How many verses in a particular book of the Bible
```bash
> echo "There are $(redis-cli keys "Genesis*" | wc -l) verses found in Genesis"
There are 1533 verses found in Genesis
```
> how many book in the Bible
```bash
redis-cli keys "*" | cut -f1 -d":" | sort | uniq | wc -l
66
```
