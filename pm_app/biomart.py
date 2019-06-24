from pybiomart import Server
server = Server(host='http://www.ensembl.org')
server.list_marts()
mart = server['ENSEMBL_MART_ENSEMBL']

from pybiomart import Dataset
dataset = Dataset(name='hsapiens_gene_ensembl',
                  host='http://www.ensembl.org')
                 
dataset.query(attributes=['ensembl_gene_id', 'external_gene_name'],
              filters={'chromosome_name': ['1','2']})
                 
                  
def attributes(self):
        
        if self._attributes is None:
            self._filters, self._attributes = self._fetch_configuration()
        return self._attributes



dataset.attributes
dataset.list_attributes()
 
def filters(self):
        if self._filters is None:
            self._filters, self._attributes = self._fetch_configuration()
        return self._filters
 
dataset.filters
dataset.list_filters()


