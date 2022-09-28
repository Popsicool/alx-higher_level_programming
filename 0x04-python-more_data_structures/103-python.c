#include <stdio.h>
#include <Python.h>

/**
* print_python_bytes - function to print python byte info
* @p: The python Object
* Return: void
*/

void print_python_bytes(PyObject *p)
{
char *str;
long int n, i, lim;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

n = ((PyVarObject *)(p))->ob_size;
str = ((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", n);
printf("  trying string: %s\n", str);

if (n >= 10)
lim = 10;
else
lim = n + 1;

printf("  first %ld bytes:", lim);

for (i = 0; i < lim; i++)
if (str[i] >= 0)
printf(" %02x", str[i]);
else
printf(" %02x", 256 + str[i]);

printf("\n");
}


/**
* print_python_list - funtion to print info of a py list
* @p: The py Object
* Return: void
*/
void print_python_list(PyObject *p)
{
long int n, i;
PyListObject *ls;
PyObject *ob;

n = ((PyVarObject *)(p))->ob_size;
ls = (PyListObject *)p;

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", n);
printf("[*] Allocated = %ld\n", ls->allocated);

for (i = 0; i < n; i++)
{
oj = ((PyListObject *)p)->ob_item[i];
printf("Element %ld: %s\n", i, ((ob)->ob_type)->tp_name);
if (PyBytes_Check(ob))
print_python_bytes(ob);
}
}
