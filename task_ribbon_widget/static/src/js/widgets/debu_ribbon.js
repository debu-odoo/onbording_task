odoo.define('task_ribbon_widget.debu_ribbon', function (require) {
    'use strict';

    var widgetRegistry = require('web.widget_registry');
    var Widget = require('web.Widget');

    var RibbonWidget = Widget.extend({
        template: 'task_ribbon_widget.debu_ribbon',
        xmlDependencies: ['/task_ribbon_widget/static/src/xml/debu_ribbon.xml'],

       
        init: function (parent, data, options) {
            this._super.apply(this, arguments);
            this.text = options.attrs.title || options.attrs.text;
            this.tooltip = options.attrs.tooltip;
            this.className = options.attrs.bg_color ? options.attrs.bg_color : 'bg-success';
            if (this.text.length > 15) {
                this.className += ' o_small';
            } else if (this.text.length > 10) {
                this.className += ' o_medium';
            }
        },
    });

    widgetRegistry.add('debu_ribbon', RibbonWidget);

    return RibbonWidget;
});
