@extends('layout')

@section('content')
    <script>

    </script>

    <div class="row">
        @foreach ($items as $item)
            <div class="col-sm-6 col-md-4">
                <div class="thumbnail" style="height: 450px">
                    <script>
                        function showImg( url ) {
                            var imgid = Math.random(), frameid = 'frameimg' + imgid;
                            window['img'+imgid] = '<img id="img" width="200px" height="200px" src=\''+url+'?kilobug\' /><script>window.onload = function() { parent.document.getElementById(\''+frameid+'\').height = document.getElementById(\'img\').height+\'px\'; }<'+'/script>';
                            document.write('<iframe id="'+frameid+'" src="javascript:parent[\'img'+imgid+'\'];" frameBorder="0" scrolling="no" width="100%"></iframe>');
                        }
                        showImg("{{ $item->img }}");
                    </script>
                    <div class="caption">
                        <h5>{{ $item->title }}</h5>
                        <p>{{ $item->content }}</p>
                        <p>
                            <a href="#" class="btn btn-primary" role="button">Button</a>
                            <a href="#" class="btn btn-default" role="button">Button</a>
                        </p>
                    </div>
                </div>
            </div>
        @endforeach
    </div>
@endsection

@section('sidebar')
    22222
@endsection