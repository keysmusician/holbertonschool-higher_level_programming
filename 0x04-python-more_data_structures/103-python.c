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
	PyListObject *list;

	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n",list->allocated);

	for (index = 0; index < len; index++)
	{
		listel = list->ob_item[index];
		printf("Element %li: %s\n", index, listel->ob_type->tp_name);
		if (PyBytes_CheckExact(listel))
			print_python_bytes(listel);
	}
}
