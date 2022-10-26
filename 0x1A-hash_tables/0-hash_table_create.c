#include "hash_tables.h"

/**
 * hash_table_create - this function creates a hash table.
 * @size: number of hash_nodes/size of array.
 * Return: pointer to the table.
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new_table;

	new_table = malloc(sizeof(hash_table_t));

	if (new_table)
		return (NULL);
	new_table->size = size;
	new_table->hash_node_t = NULL;

	return (new_table);
}
