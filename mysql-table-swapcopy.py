#!/usr/bin/env python
import argparse
import mysql.connector

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("tablename", nargs="+",
                        help="the name of one or more tables to copy")

    parser.add_argument("--shost", required=True,
                        help="the mysql source host name")

    parser.add_argument("--dhost", required=True,
                        help="the mysql destination host name")

    parser.add_argument("--sschema", required=True,
                        help="the mysql source schema name")

    parser.add_argument("--dschema", required=True,
                        help="the mysql destination schema name")

    parser.add_argument("--suser", required=True,
                        help="the username to use for the mysql source")

    parser.add_argument("--spass", required=True,
                        help="the password to use for the mysql source")\

    parser.add_argument("--duser", required=True,
                        help="the username to use for the mysql destination")

    parser.add_argument("--dpass", required=True,
                        help="the password to use for the mysql destination")

    parser.add_argument("-m", "--version-match", action="store_true",
                        help="(magento2 only) all schema versions must match for copy to run")

    args = parser.parse_args()

    source_config = {
        'user': args.suser,
        'password': args.spass,
        'host': args.shost,
        'database': args.sschema
    }

    dest_config = {
        'user': args.duser,
        'password': args.dpass,
        'host': args.dhost,
        'database': args.dschema
    }

    #if requested, check the schema data on the source and destination
    if args.version_match:
        if not magento_version_check(source_config, dest_config):
            print("Magento schema version check failed")
            exit(4)

    #run mysqldump specifying the tables listed from the source

def magento_version_check(source_config, dest_config):
    source_conn = mysql.connector.connect(**source_config)
    dest_conn = mysql.connector.connect(**dest_config)

    try:
        scursor = source_conn.cursor()
        dcursor = dest_conn.cursor()
        query = ("SELECT module, schema_version, data_version FROM setup_module;")

        scursor.execute(query)

        versions_by_module = {}
        for (module, schema_version, data_version) in scursor:
            versions_by_module[module] = (schema_version, data_version)
        scursor.close()

        dcursor.execute(query)
        for (module, schema_version, data_version) in dcursor:
            if versions_by_module.has_key(module):
                #make sure all the versions match
                version_pair = versions_by_module[module]
                if version_pair[0] != schema_version or version_pair[1] != data_version:
                    #we should not proceed
                    print("Schema " + module + " doesnt match")
                    return False


        dcursor.close()

    finally:
        source_conn.close()
        dest_conn.close()

    return True

if __name__ == "__main__":
    main()
