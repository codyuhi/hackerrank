#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_STRING_LENGTH 6

struct package
{
    char *id;
    int weight;
};

typedef struct package package;

struct post_office
{
    int min_weight;
    int max_weight;
    package *packages;
    int packages_count;
};

typedef struct post_office post_office;

struct town
{
    char *name;
    post_office *offices;
    int offices_count;
};

typedef struct town town;

void print_all_packages(town t)
{
    printf("%s:\n", t.name);
    for (int office_id = 0; office_id < t.offices_count; office_id++)
    {
        printf("\t%d:\n", office_id);
        for (int package_id = 0; package_id < t.offices[office_id].packages_count; package_id++)
        {
            printf("\t\t%s\n", t.offices[office_id].packages[package_id].id);
        }
    }
}

int get_all_packages_count(town t)
{
    int sum = 0;
    for (int office_id = 0; office_id < t.offices_count; office_id++)
    {
        sum += t.offices[office_id].packages_count;
    }

    return sum;
}

bool is_package_fitting_office(package *p, post_office *of)
{
    return (p->weight >= of->min_weight && p->weight <= of->max_weight);
}

void create_space_in_office_for_packages(post_office *of, int packages_to_add_count)
{
    of->packages = (package *)realloc(of->packages, (++of->packages_count + packages_to_add_count) * (sizeof(package)));
}

void send_package(package *p, post_office *target_office)
{
    package *received_package = &target_office->packages[target_office->packages_count - 1];
    received_package->id = (char *)malloc(MAX_STRING_LENGTH * sizeof(char));

    strcpy(received_package->id, p->id);
    received_package->weight = p->weight;
}

void shift_remaining_packages(post_office *of, int starting_index)
{
    for (int package_id = starting_index; package_id < of->packages_count; package_id++)
    {
        strcpy(of->packages[package_id - 1].id, of->packages[package_id].id);
        of->packages[package_id - 1].weight = of->packages[package_id].weight;
    }
}

void send_all_acceptable_packages(town *source, int source_office_index, town *target, int target_office_index)
{
    // source_office_index may not be starting with 0 (watch out for errors)

    post_office *target_office = &target->offices[target_office_index];
    post_office *source_office = &source->offices[source_office_index];

    for (int package_id = 0; package_id < source_office->packages_count; package_id++)
    {
        package *package_to_send = &source_office->packages[package_id];

        if (is_package_fitting_office(package_to_send, target_office))
        {
            create_space_in_office_for_packages(target_office, 1); // 1 = amount of packages that need space
            send_package(package_to_send, target_office);
            shift_remaining_packages(source_office, package_id + 1); // packade_id + 1 = starting index
            source_office->packages_count--;
            package_id--; // the last package with this index was removed and others were shifted back into its' place so loop through the same package_id again
        }
    }
}

town town_with_most_packages(town *towns, int towns_count)
{
    int town_id_most_packages = -1;
    int most_packages = -1;
    for (int town_id = 0; town_id < towns_count; town_id++)
    {
        int count = get_all_packages_count(towns[town_id]);
        if (count > most_packages)
        {
            most_packages = count;
            town_id_most_packages = town_id;
        }
    }

    return towns[town_id_most_packages];
}

town *find_town(town *towns, int towns_count, char *name)
{
    for (int town_id = 0; town_id < towns_count; town_id++)
    {
        if (strcmp(towns[town_id].name, name) == 0)
        {
            return &towns[town_id];
        }
    }

    printf("ERROR: find_town() return 0;\n");
    return (town *)0;
}

int main()
{
    int towns_count;
    scanf("%d", &towns_count);
    town *towns = malloc(sizeof(town) * towns_count);
    for (int i = 0; i < towns_count; i++)
    {
        towns[i].name = malloc(sizeof(char) * MAX_STRING_LENGTH);
        scanf("%s", towns[i].name);
        scanf("%d", &towns[i].offices_count);
        towns[i].offices = malloc(sizeof(post_office) * towns[i].offices_count);
        for (int j = 0; j < towns[i].offices_count; j++)
        {
            scanf("%d%d%d", &towns[i].offices[j].packages_count, &towns[i].offices[j].min_weight, &towns[i].offices[j].max_weight);
            towns[i].offices[j].packages = malloc(sizeof(package) * towns[i].offices[j].packages_count);
            for (int k = 0; k < towns[i].offices[j].packages_count; k++)
            {
                towns[i].offices[j].packages[k].id = malloc(sizeof(char) * MAX_STRING_LENGTH);
                scanf("%s", towns[i].offices[j].packages[k].id);
                scanf("%d", &towns[i].offices[j].packages[k].weight);
            }
        }
    }
    int queries;
    scanf("%d", &queries);
    char town_name[MAX_STRING_LENGTH];
    while (queries--)
    {
        int type;
        scanf("%d", &type);
        switch (type)
        {
        case 1:
            scanf("%s", town_name);
            town *t = find_town(towns, towns_count, town_name);
            print_all_packages(*t);
            break;
        case 2:
            scanf("%s", town_name);
            town *source = find_town(towns, towns_count, town_name);
            int source_index;
            scanf("%d", &source_index);
            scanf("%s", town_name);
            town *target = find_town(towns, towns_count, town_name);
            int target_index;
            scanf("%d", &target_index);
            send_all_acceptable_packages(source, source_index, target, target_index);
            break;
        case 3:
            printf("Town with the most number of packages is %s\n", town_with_most_packages(towns, towns_count).name);
            break;
        }
    }
    return 0;
}