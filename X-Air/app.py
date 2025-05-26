""" Command-line utility to link or unlink channel pairs on a Behringer X Air XR18 mixer."""
import argparse
import xair_api


def parse_args():
    """
    Parse command-line arguments for controlling Behringer X Air mixer linking.

    Returns:
        argparse.Namespace: Parsed arguments containing the following:
            - action (str): The action to perform, either "link" or "unlink".
            - channelpair (str): The channel pair to link or unlink. 
              Choices are: "1-2", "3-4", "5-6", "7-8", "9-10", "11-12", "13-14", "15-16".
            - ip (str): The IP address of the mixer (required).
    """
    parser = argparse.ArgumentParser(
        description="Control Behringer X Air mixer linking.")
    parser.add_argument("action", choices=[
                        "link", "unlink"], help="What action to perform")
    parser.add_argument("channelpair", choices=[
        "1-2", "3-4", "5-6", "7-8", "9-10", "11-12", "13-14", "15-16"
    ], help="Channel pair to link or unlink")
    parser.add_argument("--ip", required=True, help="IP address of the mixer")
    return parser.parse_args()


def main():
    """
    Main function to handle linking or unlinking of channel pairs on an XR18 mixer.

    This function parses command-line arguments to determine the channel pair and the action 
    (link or unlink). It then connects to the XR18 mixer using the specified IP address, 
    checks if the channel pair is valid, and performs the requested action.

    Raises:
        ValueError: If the specified channel pair is invalid.

    Prints:
        A message indicating whether the channel pair was linked or unlinked.
    """
    args = parse_args()
    attr = f"chlink{args.channelpair.replace('-', '_')}"

    with xair_api.connect("XR18", ip=args.ip) as mixer:
        if not hasattr(mixer.config, attr):
            raise ValueError(f"Ugyldig kanalpar: {args.channelpair}")

        setattr(mixer.config, attr, args.action == "link")
        print(f"{args.channelpair} {'linket' if args.action == 'link' else 'unlinket'}.")



if __name__ == "__main__":
    main()
