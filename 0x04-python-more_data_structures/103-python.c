#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_bytes - Print information about python bytes objects.
 * @p: python object pointer (expecting bytes object)
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbop; // PyBytesObject pointer
	Py_ssize_t size, i;

	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
		printf("  size: %li\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));

	// Cap size at 10 bytes for the following loop
	size = size > 10 ? 10 : size + 1;
	pbop = (PyBytesObject *)p;
		printf("  first %li bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02x", 0xff & pbop->ob_sval[i]);
	printf("\n");
}

/**
 * print_python_list - Print information about python list objects.
 * @p: Python object pointer (expecting list object)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t index, len = PyList_Size(p);
	PyObject *listel;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %i\n", 0); /* Incorrect; Find the correct function */

	for (index = 0; index < len; index++)
	{
		listel = PyList_GetItem(p, index); // Replace this function
		printf("Element %li: %s\n",
				index, Py_TYPE(listel)->tp_name); // Don't use Py_TYPE
		if (PyBytes_CheckExact(listel))
			print_python_bytes(listel);
	}
}
