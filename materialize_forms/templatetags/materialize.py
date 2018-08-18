from django import template
from django.forms import widgets
from django.forms.fields import DateField, TimeField, CharField
from django.template import Context
from django.template.loader import get_template
from django.utils.html import escape
from django.utils.safestring import mark_safe

from phonenumber_field.formfields import PhoneNumberField

register = template.Library()


def add_css_class_widget(widget, css_class):
    if 'class' in widget.attrs:
        _css_class = '%s %s' % (widget.attrs['class'], css_class)
    else:
        _css_class = css_class
    widget.attrs['class'] = _css_class


@register.filter
def as_material(field, col='s6'):
    try:
        widget = field.field.widget
    except:
        raise ValueError("Expected a Field, got a %s" % type(field))

    try:
        clazz = {'class': widget.attrs['class'] + ' validate'}
    except KeyError:
        clazz = {'class': 'validate'}
    widget.attrs.update(clazz)

    # Because the above has already run, we can be sure the
    # widget.attrs['class'] key is already present
    if field.errors:
        # There are django field errors, so add the invalid class to
        # mark the field invalid in materialize
        clazz = {'class': widget.attrs['class'] + ' invalid'}
    widget.attrs.update(clazz)
    if isinstance(field.field, PhoneNumberField):
        widget.input_type = u'tel'
        if field.help_text:
            placeholder_attr = {'placeholder': field.help_text}
            widget.attrs.update(placeholder_attr)

    if isinstance(field.field, CharField) and field.help_text:
        placeholder_attr = {'placeholder': field.help_text}
        widget.attrs.update(placeholder_attr)
    
    if isinstance(field.field, DateField):
        input_type = u'date'
        add_css_class_widget(widget, 'datepicker')
        widget.input_type = 'date'
    elif isinstance(field.field, TimeField):
        input_type = u'time'
        add_css_class_widget(widget, 'timepicker')
        widget.input_type = 'time'
    else:
        try:
            input_type = widget.input_type
        except AttributeError:
            if isinstance(widget, widgets.Textarea):
                input_type = u'textarea'
                add_css_class_widget(widget, 'materialize-textarea')
            elif isinstance(widget, widgets.CheckboxInput):
                input_type = u'checkbox'
            elif isinstance(widget, widgets.CheckboxSelectMultiple):
                input_type = u'multicheckbox'
            elif isinstance(widget, widgets.RadioSelect):
                input_type = u'radio'
            elif isinstance(widget, widgets.Select):
                input_type = u'select'
            else:
                input_type = u'default'

    return get_template("materialize/field.html").render({
        'field': field,
        'col': col,
        'input_type': input_type,
    })


@register.filter
def html_attrs(attrs):
    pairs = []
    for name, value in attrs.items():
        pairs.append(u'%s="%s"' % (escape(name), escape(value)))
    return mark_safe(u' '.join(pairs))
