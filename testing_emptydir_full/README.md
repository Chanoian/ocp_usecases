# testing_emptydir_full

This will test what will happens when the emptyDir gets over sizeLimit using 
dd if=/dev/urandom of=test1 bs=1M count=10240

# Findings

The pod will be evicted if it reaches the sizeLimit
