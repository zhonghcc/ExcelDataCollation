# -*- coding: utf-8 -*-
import sys
import io
import os
import xlwt
import traceback
import logging
import logging.config

from PyQt4 import QtGui
from PyQt4 import *
import gui.mainWindow

if __name__ == '__main__':
    logging.config.fileConfig('logging.conf')

    # create logger
    logger = logging.getLogger('DataCollation')

    # 'application' code
    logger.info('=======================================')
    logger.info('App Start...')
    #Qt is the master
    app = QtGui.QApplication(sys.argv)

    gui.mainWindow.MainWindow(None).start()

    sys.exit(app.exec_())

