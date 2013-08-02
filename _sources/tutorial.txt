########
TUTORIAL
########

1. Install WorkFlowRepr

.. code-block:: bash

    $ pip install -e git+https://github.com/xiechao06/WorkFlowRepr.git#egg=work_flow_repr-dev

2. Specify how to represent the node

.. code-block:: python
    
    class Order(db.Model):
        __tablename__ = 'TB_ORDER'

        id = db.Column(db.Integer, primary_key=True)

    class WorkCommand(db.Model):
        __tablename__ = 'TB_WORK_COMMAND'

        id = db.Column(db.Integer, primary_key=True)
        order_id = db.Column(db.Integer, db.ForeignKey("TB_ORDER.id"))
        order = db.relationship("Order", backref='work_command_list')

    class OrderModelNode(ModelNode):

        @property
        def description(self):
            return 'an <strong>order</strong> is a commitment made to customer'

        @property
        def target(self):
            return '/order/' + str(self.obj.id)

        @property
        def events(self):
            return [
                Event(datetime.strptime('2013-08-01 10:00:00', "%Y-%m-%d %H:%M:%S"), 'create', 'manager'),
                Event(datetime.strptime('2013-08-01 10:30:00', "%Y-%m-%d %H:%M:%S"), 'split to work commands', 'manager'),
            ]

        @property
        def children_model_groups(self):
            return [('work command list', self.obj.work_command_list)]

    class WorkCommandModelNode(ModelNode):
        
        @property
        def children_model_groups(self):
            return []

        @property
        def target(self):
            return '/work_command/' + str(self.obj.id)

        @property
        def events(self):
            return [
                Event(datetime.strptime('2013-08-01 10:30:00', "%Y-%m-%d %H:%M:%S"), 'create', 'worker', by='split to work command'),
                Event(datetime.strptime('2013-08-01 17:30:00', "%Y-%m-%d %H:%M:%S"), 'finish', 'worker'),
            ]

        @property
        def name(self):
            return 'WC'

    annotate(Order, OrderModelNode)
    annotate(WorkCommand, WorkCommandModelNode)

3. Pass the tree as a template parameter

.. code-block:: python


    app = Flask(__name__)

    @app.route('/order-tree')
    def order_tree(id_):
        order = Order.query.get(id_)
        return render_template('order-tree.html', tree=make_tree(order))

4. In template, represent the work flow DAG

.. code-block:: html

    <!DOCTYPE HTML>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title></title>
      <link rel="stylesheet" href="{{ url_for('static', filename='bootstrap/css/bootstrap.min.css') }}" />
      <link rel="stylesheet" href="{{ url_for('static', filename='css/opentip.css') }}" />
      <script type="text/javascript" src="{{ url_for('static', filename='js/svg.min.js') }}"></script>
      <script type="text/javascript" src="{{ url_for('static', filename='js/svg.foreignobject.js') }}"></script>
      <script type="text/javascript" src="{{ url_for('static', filename='js/jquery.min.js') }}"></script>
      <script type="text/javascript" src="{{ url_for('static', filename='js/opentip-jquery.min.js') }}"></script>
      <script type="text/javascript" src="{{ url_for('static', filename='bootstrap/js/bootstrap.min.js') }}"></script>
      <script type="text/javascript" src="{{ url_for('static', filename='js/work-flow-repr.js') }}"></script>
      <script type="text/javascript">
        $(function () {
          var tree = {{ tree|tojson|safe }};
          var canvas = document.getElementById('canvas');
          var workFlowRepr = new WorkFlowRepr(canvas, tree, 10);
          workFlowRepr.draw();
        });
      </script>
    </head>
    <body>
      <div id="canvas"></div>
    </body>
    </html>

Then visit the page, see what happens.
