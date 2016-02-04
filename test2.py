import sdoc
from sdoc.sdoc1.SDoc1Interpreter import SDoc1Interpreter
from sdoc.sdoc2.SDoc2Interpreter import SDoc2Interpreter

sdoc1 = SDoc1Interpreter()
sdoc1.process('test2.sdoc', 'test2.tmp')

sdoc2 = SDoc2Interpreter()
sdoc2.process('test2.tmp', 'test2.html')

#sdoc.sdoc2.node_store.nodes[1].print_info(0)
sdoc.sdoc2.node_store.generate_html()