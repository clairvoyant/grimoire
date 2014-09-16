/*****************************************************************************
* File:  main.c
* 
* Description: ......
*
* 
*
*****************************************************************************/

#include <json/json.h>
#include <json/json_object.h>
#include <iostream>
#include <stdlib.h>


void
usage(const char* log)
{
   std::cerr << log << std::endl;
   std::cerr << "Usage: executable filename.json" << std::endl;
   exit(-1);

}

int
json_to_cfg(struct json_object* cfg)
{
   int result = 0;

   //if (json_object_get_type(cfg)==json_type_object) {
    enum json_type type;
    json_object_object_foreach(cfg, key, val) {
        type = json_object_get_type(val);
        std::cout << "key: " << key << std::endl;
        switch (type) {
            case json_type_null: 
                                 std::cout << "\tjson_type_null: " << std::endl;
                                 break;
            case json_type_boolean: 
                                std::cout << "\tjson_type_boolean: " << json_object_get_boolean(val) << std::endl;
                                break;
            case json_type_double: 
                                std::cout << "\tjson_type_double: " << json_object_get_double(val) << std::endl;
                                break;
            case json_type_int: 
                                   std::cout << "\tjson_type_int: " <<  json_object_get_int(val) << std::endl;
                                break;
            case json_type_object: 
                                std::cout << "\tjson_type_object" << std::endl;
                                json_to_cfg(val);
                                   break;
            case json_type_array: { 
                                      std::cout << "\tjson_type_array" << std::endl;
                                      int len = json_object_array_length(val);
                                      for (int i=0; i<len; i++) {
                                          json_to_cfg(json_object_array_get_idx(val, i));
                                      }
                                  }
                                  break;
            case json_type_string: 
                                 std::cout << "\tjson_type_string: " << json_object_get_string(val) <<  std::endl;
                                 break;
        }
    //}
   }

   return result;
}

int 
main (int argc, char ** argv)
{
    int i;

    std::cout << "argc:" << argc <<std::endl;

    if (argc<2) 
       usage("");

    
    for(i=1; i<argc; ++i) {
        
        std::cout << "parsing:" << argv[i] <<std::endl;
        struct json_object* cfg = json_object_from_file(argv[i]);

        if (cfg!=NULL) {
           json_to_cfg(cfg);
        }
    }

    return 0;
}
