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

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", Py_SIZE(p)); /* Incorrect */

	for (index = 0; index < len; index++)
	{
		printf("Element %li: %s\n",
		index, Py_TYPE(PyList_GetItem(p, index))->tp_name);
	}
}
