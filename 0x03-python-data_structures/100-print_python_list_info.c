#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - utilizes the python/C API to print information
 * about python lists.
 *
 * @p: Python object pointer (expecting list object)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t index, len = PyList_Size(p);
	PyListObject *list;

	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", list->allocated); /* Incorrect */

	for (index = 0; index < len; index++)
	{
		printf("Element %li: %s\n", index,
			list->ob_item[index]->ob_type->tp_name);
	}
}
