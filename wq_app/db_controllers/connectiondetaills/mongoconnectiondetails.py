from wq_project.db_controllers.connectiondetaills.connectiondetailsbase import ConnectionDetailsBase


class MongoConnectionDetails(ConnectionDetailsBase):
    """
    Connection details for a Mongo server
    """

    def __init__(self, hosts):
        """
        Initializes the Mongo connection details object
        :param hosts: The host details of the Mongo server
        :type hosts: list[str]
        """
        self.hosts = hosts
