def before_all(context):
    context.config.userdata={}


def before_scenario(context):
    context.token_value=context.config.userdata('token_value',None)

