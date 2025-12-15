def cloud_factory(provider):
    if provider == "aws":
        return AWSClient()
    elif provider == "gcp":
        return GCPClient()
    
cloud = cloud_factory("aws")
