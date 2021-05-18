#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <stdio.h>

/**
 * print_python_bytes - Print information about python bytes objects.
 * @p: python object pointer (expecting bytes object)
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *pbop; // PyBytesObject pointer
	Py_ssize_t size, i;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	pbop = (PyBytesObject *)p;

	size = PyBytes_Size(p);
	printf("  size: %li\n", size);
	printf("  trying string: %s\n", pbop->ob_sval);

	// Cap size at 10 bytes for the following loop
	size = size > 10 ? 10 : size + 1;
	printf("  first %li bytes:", size);
	for (i = 0; i < size; i++)
		printf(" %02x", 0xff & pbop->ob_sval[i]);
	printf("\n");
}

/**
 * print_python_float - Print information about python float objects.
 * @p: python object pointer (expecting float object)
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *pyflop; // PyFloatObject pointer
	double value;

	pyflop = (PyFloatObject *)p;
	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(pyflop))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = PyFloat_AsDouble(p);
	printf("	value: %.1f\n", value);
}

/**
 * print_python_list - Print information about python list objects.
 * @p: Python object pointer (expecting list object)
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t index, len;
	PyVarObject *varlist;
	PyObject *listel;
	PyListObject *list;

	list = (PyListObject *)p;
	varlist = (PyVarObject *)p;
	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (!PyList_CheckExact(list))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	len = varlist->ob_size;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", list->allocated);

	for (index = 0; index < len; index++)
	{
		listel = list->ob_item[index];
		printf("Element %li: %s\n", index, listel->ob_type->tp_name);
		if (PyBytes_CheckExact(listel))
			print_python_bytes(listel);
		else if (PyFloat_CheckExact(listel))
			print_python_float(listel);
	}
}
