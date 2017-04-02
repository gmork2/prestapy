import argparse
import pkg_resources


def app():
    parser = argparse.ArgumentParser(description='Loads a plugin')
    parser.add_argument('action', choices=['run', 'list'],
                        help='action to be performed')
    parser.add_argument('-p', '--plugin',
                        help='plugin to be loaded')
    args = parser.parse_args()

    if args.action == 'list':
        full_env = pkg_resources.Environment()
        dists, errors = pkg_resources.WorkingSet().find_plugins(full_env)
        for dist in dists:
            if 'plugin_system' in dist.get_entry_map():
                print('  %s (%s)' % (dist.project_name, dist.version))
    elif args.action == 'run':
        requirement = pkg_resources.Requirement(args.plugin)
        plugin = pkg_resources.WorkingSet().find(requirement)
        main = plugin.load_entry_point('plugin_system', 'main')
        main()

if __name__ == '__main__':
    app()

