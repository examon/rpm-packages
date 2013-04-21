#!/bin/bash

github_dir="/home/exo/Github/rpm-packages"
rpmbuild_dir="/home/exo/rpmbuild"

cp $github_dir/fedora-gooey-karma/fedora-gooey-karma.spec $rpmbuild_dir/SPECS

cd $rpmbuild_dir/SOURCES
git clone git://github.com/examon/fedora-gooey-karma.git
tar cvzf fedora-gooey-karma.tar.gz fedora-gooey-karma
cd ..

rpmbuild -ba SPECS/fedora-gooey-karma.spec
cp SPECS/fedora-gooey-karma.spec $github_dir/fedora-gooey-karma/
cp RPMS/noarch/fedora-gooey-karma* $github_dir/fedora-gooey-karma/
