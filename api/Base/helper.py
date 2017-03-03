import json
import sqlalchemy


def to_dict(item):
    """Converts a single sqlalchemy object to dictionary."""
    columns = item.__table__.columns
    columns_names = columns.keys()

    def _to_dict(item, column_name, d):
        column_type = type(columns[column_name].type)
        if column_type == sqlalchemy.types.Time:
            d.update({column_name: item.__getattribute__(column_name).strftime("%I:%M %p")})
        elif column_type == sqlalchemy.types.DateTime:
            d.update({column_name: item.__getattribute__(column_name).strftime("%a, %m/%d/%y")})
        else:
            d.update({column_name: item.__getattribute__(column_name)})

    result = {}

    for column in columns_names:
        if column != 'id':
            _to_dict(item, column, result)

    return result


def to_json(items):
    """Converts a list or single sqlalchemy object(s) to JSON."""

    if type(items) == list:
        result = []
        for item in items:
            result.append(to_dict(item))
    elif items == {}:
        result = items
    else:
        result = to_dict(items)

    return json.dumps(result)
