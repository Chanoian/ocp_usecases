# Testing what is the termination type that Kubernetes will send to the pods that exceeds the storage limit



# Findings:
I'ts SigTerm within a grace period of 10 seconds by default if the app doesn't kill then SigKill