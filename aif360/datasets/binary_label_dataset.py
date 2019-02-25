from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from aif360.datasets import StructuredDataset


class BinaryLabelDataset(StructuredDataset):
    """Base class for all structured datasets with binary labels."""

    def __init__(self, favorable_label=1., unfavorable_label=0., **kwargs):
        """
        Args:
            favorable_label (float): Label value which is considered favorable
                (i.e. "positive").
            unfavorable_label (float): Label value which is considered
                unfavorable (i.e. "negative").
            **kwargs: StructuredDataset arguments.
        """
        self.favorable_label = float(favorable_label)
        self.unfavorable_label = float(unfavorable_label)

        super(BinaryLabelDataset, self).__init__(**kwargs)

    def validate_dataset(self):
        """Error checking and type validation.

        Raises:
            ValueError: `labels` must be shape [n, 1].
            ValueError: `favorable_label` and `unfavorable_label` must be the
                only values present in `labels`.
        """
        super(BinaryLabelDataset, self).validate_dataset()

        # =========================== SHAPE CHECKING ===========================
        # Verify if the labels are only 1 column
        if self.labels.shape[1] != 1:
            raise ValueError("BinaryLabelDataset only supports single-column "
                "labels:\n\tlabels.shape = {}".format(self.labels.shape))

        # =========================== VALUE CHECKING ===========================
        # Check if the favorable and unfavorable labels match those in the dataset
        if (set([self.favorable_label, self.unfavorable_label])
                != set(self.labels.ravel())):
            raise ValueError("The favorable and unfavorable labels provided do "
                             "not match the labels in the dataset.")
