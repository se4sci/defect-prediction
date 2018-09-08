"""
A data handler class to read and process data
"""

import os
import sys
import pandas as pd
from glob2 import glob
from pathlib import Path
from pdb import set_trace

root = Path(os.path.abspath(os.path.join(
    os.getcwd().split("se4sci")[0], 'se4sci/se4sci')))

if root not in sys.path:
    sys.path.append(str(root))


class DataHandler:
    """
    A Generic data handler class

    Parameters
    ----------
    data_path = <pathlib.PosixPath>
        Path to the data folder.
    """

    def __init__(self, data_path=root.joinpath("data")):
        self.data_path = data_path

    def get_data(self):
        """
        Read data as pandas and return a dictionary of data

        Parameters
        ----------

        Returns
        -------
        all_data: dict
            A dictionary of data with key-project_name, value-dictionary of 
            {release_version, metrics_defects}
        
        Example
        -------
        
        """
        all_data = dict()
        projects = [Path(proj) for proj in glob(
            str(self.data_path.joinpath("[!_]*"))) if Path(proj).is_dir()]

        for project in projects:
            all_data.update({project.name: [pd.read_csv(ver) for ver in glob(str(project.joinpath("**/*_file_metrics*_1.csv")))]})

        return all_data