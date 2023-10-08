#include <Python.h>

/**
 * print_python_list_info - Basic info about Python lists.
 * @p: A PyObject list of python.
 */
void print_python_list_info(PyObject *p)
{
	int alloc, size, j;
	PyObject *obj;
	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python List size = %d\n", size);
	printf("[*] Allocate = %d\n", alloc);

	for (j = 0; j < size; j++)
	{
		printf("The element %d: ", j);

		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
