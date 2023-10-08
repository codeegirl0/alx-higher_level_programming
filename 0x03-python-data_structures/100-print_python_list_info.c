#include <Python.h>

/**
 * print_python_list_info - Some basic info about list in Python.
 * @q: List of PyObject.
 */
void print_python_list_info(PyObject *q)
{
	int mysize, allocate, j;
	PyObject *myobj;

	mysize= Py_SIZE(q);
	allocate = ((PyListObject *)q)->allocated;

	printf("[*] Python List Size = %d\n", mysize);
	printf("[*] Allocated = %d\n", allocate);

	for (j = 0; j < mysize; j++)
	{
		printf("The element %d: ", j);

		myobj = PyList_GetItem(q, j);
		printf("%s\n", Py_TYPE(myobj)->tp_name);
	}
}
