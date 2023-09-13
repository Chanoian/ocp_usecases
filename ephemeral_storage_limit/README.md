# Testing ephemeral storage in K8S with the Request and Limit

See how K8S will react to ephemeral storage limit


# Findings

K8S will look into the Request/Limit for Ephemeral storage as the total amount of the storage used by the container including emptyDir volume mounts and all the other local file system