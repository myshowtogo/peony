#ifndef PEONYQTMENUPLUGINEXAMPLE_GLOBAL_H
#define PEONYQTMENUPLUGINEXAMPLE_GLOBAL_H

#include <QtCore/qglobal.h>

#if defined(PEONYQTMENUPLUGINEXAMPLE_LIBRARY)
#  define PEONYQTMENUPLUGINEXAMPLESHARED_EXPORT Q_DECL_EXPORT
#else
#  define PEONYQTMENUPLUGINEXAMPLESHARED_EXPORT Q_DECL_IMPORT
#endif

#endif // PEONYQTMENUPLUGINEXAMPLE_GLOBAL_H
