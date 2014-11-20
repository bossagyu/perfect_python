try:
    import json
except ImportError as ie:
    try:
        import simplejson as json
    except ImportError as iee:
        print ('''can't import json ibrary''')
        raise

