


def owner_check(ctx):
    _id = ctx.author.id

    return _id == 349602653107388416 or ctx.author.guild_permissions.administrator